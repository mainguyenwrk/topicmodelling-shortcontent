library(stm)
library(readr)

# Read the CSV file 
influencer_narratives_text <- read_csv(updated_file)

# Clean and preprocess the text
influencer_narratives_text <- tibble(
  transcription = influencer_narratives$transcription,
)

# Tokenize and count words
tidy_influencer_narratives <- influencer_narratives_text %>%
  mutate(postID = row_number()) %>%
  unnest_tokens(word, transcription) %>%
  count(word)

# Create a sparse matrix
influencer_narratives_sparse <- tidy_influencer_narratives %>%
  count(postID) %>%
  cast_sparse(postID, n)

# Train topic models with different numbers of topics
many_models <- tibble(K = c(2)) %>%
  mutate(topic_model = future_map(K, ~stm(influencer_narratives_sparse, K = ., 
                                          verbose = FALSE)))

# Evaluate the topic models
heldout <- make.heldout(influencer_narratives_sparse)

k_result <- many_models %>%
  mutate(exclusivity = map(topic_model, ~stm::exclusivity(.x)),
         semantic_coherence = map(topic_model, semanticCoherence, influencer_narratives_sparse),
         eval_heldout = map(topic_model, eval.heldout, heldout$missing),
         residual = map(topic_model, checkResiduals, influencer_narratives_sparse),
         bound = map_dbl(topic_model, function(x) max(x$convergence$bound)),
         lfact = map_dbl(topic_model, function(x) lfactorial(x$settings$dim$K)),
         lbound = bound + lfact,
         iterations = map_dbl(topic_model, function(x) length(x$convergence$bound)))

# Display the results
k_result

# Plot model diagnostics
k_result %>%
  transmute(K,
            `Lower bound` = lbound,
            Residuals = map_dbl(residual, "dispersion"),
            `Semantic coherence` = map_dbl(semantic_coherence, mean),
            `Held-out likelihood` = map_dbl(eval_heldout, "expected.heldout")) %>%
  gather(Metric, Value, -K) %>%
  ggplot(aes(K, Value, color = Metric)) +
  geom_line(size = 1.5, alpha = 0.7, show.legend = FALSE) +
  facet_wrap(~Metric, scales = "free_y") +
  labs(x = "K (number of topics)",
       y = NULL,
       title = "Model diagnostics by number of topics",
       subtitle = "These diagnostics indicate that a good number of topics would be around 60")

# Compare exclusivity and semantic coherence
k_result %>%
  select(K, exclusivity, semantic_coherence) %>%
  filter(K %in% c(20, 40, 70)) %>%
  unnest() %>%
  mutate(K = as.factor(K)) %>%
  ggplot(aes(semantic_coherence, exclusivity, color = K)) +
  geom_point(size = 2, alpha = 0.7) +
  labs(x = "Semantic coherence",
       y = "Exclusivity",
       title = "Comparing exclusivity and semantic coherence",
       subtitle = "Models with fewer topics have higher semantic coherence for more topics, but lower exclusivity")

# Clean and preprocess the text using the textProcessor function from the stm package
processedData <- textProcessor(influencer_narratives$transcription, metadata = influencer_narratives)

# Create the document-term matrix and remove extremely common and rare terms
documents <- processedData$documents
meta <- processedData$meta
vocab <- processedData$vocab
out <- prepDocuments(documents, vocab, meta)

# Store the document-term matrix, meta data, and vocabulary separately
doc_term_matrix <- out$documents
meta_data <- out$meta
vocab <- out$vocab

# Fit the STM model with covariates
First_STM <- stm(documents = doc_term_matrix,
                 vocab = vocab,
                 K = 3,
                 data = meta_data,
                 max.em.its = 75,
                 init.type = "Spectral",
                 verbose = FALSE,
                 prevalence = ~Gender)

# Plot the STM results
plot(First_STM)

# Print completion message
print('done')
