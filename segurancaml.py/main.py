from data.stream_simulator import stream_data
from models.online_model import OnlineDefensiveModel
from defense.decision_engine import decide
from defense.response_system import respond
model = OnlineDefensiveModel()

print("🛡️ Sistema Defensivo Online iniciado...\n")

for X, y in stream_data():

    if model.initialized:
        prediction = model.predict(X)[0]
        probability = model.predict_proba(X)[0][1]

        action = decide(prediction, probability)
        respond(action)

        print(f"Predição: {prediction} | Confiança: {probability:.2f}\n")

    model.update(X, [y])
