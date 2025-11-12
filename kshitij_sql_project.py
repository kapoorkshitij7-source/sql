# Load libraries
library(ggplot2)

# Read CSV file
data <- read.csv("student_data.csv")

# View first few rows
print(head(data))

# Summary statistics
print(summary(data))

# Correlation between study hours and marks
correlation <- cor(data$StudyHours, data$Marks)
cat("Correlation between Study Hours and Marks:", correlation, "\n")

# Linear Regression Model
model <- lm(Marks ~ StudyHours + Attendance, data=data)
cat("Model Summary:\n")
print(summary(model))

# Scatter plot (StudyHours vs Marks)
ggplot(data, aes(x=StudyHours, y=Marks)) +
  geom_point(color="blue", size=3) +
  geom_smooth(method="lm", se=FALSE, color="red") +
  ggtitle("Study Hours vs Marks") +
  xlab("Study Hours") + ylab("Marks")

# Boxplot for Attendance vs Marks
ggplot(data, aes(x=factor(round(Attendance/10)*10), y=Marks)) +
  geom_boxplot(fill="orange") +
  ggtitle("Attendance Group vs Marks") +
  xlab("Attendance Group (%)") + ylab("Marks")
