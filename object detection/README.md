Thank for IBM service, we visual-recognition on watsonplatform, you can use our model with following link:

https://gateway.watsonplatform.net/visual-recognition/api


Authentication
```
curl -u "apikey:{apikey}" "https://gateway.watsonplatform.net/visual-recognition/api/v3/{method}"
```
Classify an image (GET)
```
curl -u "apikey:{apikey}" "https://gateway.watsonplatform.net/visual-recognition/api/v3/classify?url=https://watson-developer-cloud.github.io/doc-tutorial-downloads/visual-recognition/fruitbowl.jpg&version=2018-03-19&classifier_ids=DefaultCustomModel_1428719196"
```
Classify an image (POST)
```
curl -X POST -u "apikey:{apikey}" -F "images_file=@fruitbowl.jpg" -F "threshold=0.6" -F "classifier_ids=DefaultCustomModel_1428719196" "https://gateway.watsonplatform.net/visual-recognition/api/v3/classify?version=2018-03-19"
```
