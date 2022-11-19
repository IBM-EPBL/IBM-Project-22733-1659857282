model = svm.SVC(kernel='linear')

# training the SVM model with training data
model.fit(X_train, Y_train)

SVC(kernel='linear')
