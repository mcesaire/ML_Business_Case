from preprocessing import preprocessing
from train import feature_extractor, train
from predict import predict

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

##### Feature extraction #####

X, Y = preprocessing("./datasets/entreprise_1/")
X = feature_extractor(X)

##### Train step #####

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)

# Save trained model and load it
train(X_train, y_train, RandomForestRegressor(n_estimators=10, warm_start=True, oob_score=True, n_jobs=-1))

##### Prediction and results #####
print(predict(X_train, X_test, y_train, y_test))

