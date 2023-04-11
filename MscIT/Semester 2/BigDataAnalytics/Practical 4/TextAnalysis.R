# Read in the data
dataset_original <- read.delim("F:\\GitHub\\Practical_BscIT_MscIT_Ninad\\MscIT\\Semester 2\\BigDataAnalytics\\Dataset\\Restaurant_Reviews.tsv", quote = "", stringsAsFactors = FALSE)
head(dataset_original)
# Install and load required packages
install.packages('tm')
install.packages('SnowballC')
install.packages('randomForest')
library(tm)
library(SnowballC)
library(caTools)
library(randomForest)

# Create a corpus
corpus <- VCorpus(VectorSource(dataset_original$Review))
corpus <- tm_map(corpus, content_transformer(tolower))
corpus <- tm_map(corpus, removeNumbers)
corpus <- tm_map(corpus, removePunctuation)
corpus <- tm_map(corpus, removeWords, stopwords())
corpus <- tm_map(corpus, stemDocument)
corpus <- tm_map(corpus, stripWhitespace)

# Create a document term matrix
dtm <- DocumentTermMatrix(corpus)
dtm <- removeSparseTerms(dtm, 0.999)

# Convert the dtm to a data frame
dataset <- as.data.frame(as.matrix(dtm))
dataset$Liked <- dataset_original$Liked
dataset$Liked <- factor(dataset$Liked, levels = c(0,1))

# Split the data into training and test sets
set.seed(123)
split <- sample.split(dataset$Liked, SplitRatio = 0.8)
training_set <- subset(dataset, split == TRUE)
test_set <- subset(dataset, split == FALSE)

# Train a random forest classifier
classifier <- randomForest(x = training_set[-692], y = training_set$Liked, ntree = 10)

# Make predictions on the test set and create a confusion matrix
y_pred <- predict(classifier, newdata = test_set[-692])
cm <- table(test_set[,692], y_pred)
print(cm)
