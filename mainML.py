import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score
import joblib

def load_dataset(filepath):
    """Load the chatbot response dataset from CSV."""
    try:
        # Use `quotechar` and `escapechar` to handle commas in the fields
        df = pd.read_csv(filepath, quotechar='"', escapechar='\\')
        return df
    except pd.errors.ParserError as e:
        print(f"Error parsing the CSV file: {e}")
        return None

def train_model(df):
    """Train the machine learning model on the given dataset."""
    X = df['User_Message']
    y = df['Reply']

    # Split dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a pipeline: TF-IDF vectorization + Logistic Regression
    model = make_pipeline(TfidfVectorizer(), LogisticRegression())

    # Train the model
    model.fit(X_train, y_train)

    # Test the model and print accuracy
    y_pred = model.predict(X_test)
    print(f"Test Accuracy: {accuracy_score(y_test, y_pred)}")

    # Return the trained model
    return model

def save_model(model, filepath):
    """Save the trained model to a file."""
    joblib.dump(model, filepath)
    print(f"Model saved to {filepath}")

def main():
    # Load dataset
    dataset = load_dataset('modified_chat_responses.csv')
    
    if dataset is not None:
        # Train the model
        trained_model = train_model(dataset)
        
        # Save the model to disk
        save_model(trained_model, 'chatbot_response_model.pkl')

if __name__ == '__main__':
    main()
