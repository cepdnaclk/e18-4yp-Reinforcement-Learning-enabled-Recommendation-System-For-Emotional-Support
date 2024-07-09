import React, { useState } from "react";
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  Alert,
  Image,
  ActivityIndicator,
} from "react-native";

export default function Home({ route, navigation }) {
  const { username, userid } = route.params;
  const [emotion, setEmotion] = useState("");
  const [loading, setLoading] = useState(false);

  const handleEmotionSelect = (selectedEmotion) => {
    setEmotion(selectedEmotion);
    setLoading(true);

    fetch(`http://10.0.2.2:5000/get-suggestions`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        userid: userid,
        emotion: selectedEmotion,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        setLoading(false);
        if (data.suggestions) {
          navigation.navigate("Suggestion", {
            suggestions: data.suggestions,
            userid: userid,
          });
        } else {
          Alert.alert("No suggestions available");
        }
      })
      .catch((error) => {
        setLoading(false);
        console.error("Error:", error);
        Alert.alert("An error occurred while fetching suggestions");
      });
  };

  return (
    <View style={styles.container}>
      <Image
        style={{ width: 100, height: 100 }}
        source={require("./assets/hello.gif")}
      />
      <Text style={styles.greeting}>Hello, {username}!</Text>
      <Text style={styles.question}>How are you feeling today?</Text>
      <View style={styles.buttonContainer}>
        {loading ? (
          <ActivityIndicator size="large" color="red" />
        ) : (
          <>
            <TouchableOpacity
              style={[styles.button, styles.happyButton]}
              onPress={() => handleEmotionSelect("Happy")}
            >
              <Text style={styles.buttonText}>😊 Happy</Text>
            </TouchableOpacity>
            <TouchableOpacity
              style={[styles.button, styles.sadButton]}
              onPress={() => handleEmotionSelect("Sad")}
            >
              <Text style={styles.buttonText}>😢 Sad</Text>
            </TouchableOpacity>
            <TouchableOpacity
              style={[styles.button, styles.stressedButton]}
              onPress={() => handleEmotionSelect("Stressed")}
            >
              <Text style={styles.buttonText}>😫 Stressed</Text>
            </TouchableOpacity>
            <TouchableOpacity
              style={[styles.button, styles.relaxedButton]}
              onPress={() => handleEmotionSelect("Relaxed")}
            >
              <Text style={styles.buttonText}>😌 Relaxed</Text>
            </TouchableOpacity>
          </>
        )}
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    padding: 20,
    backgroundColor: "#f5f5f5",
  },
  greeting: {
    fontSize: 30,
    marginBottom: 20,
    color: "#333",
    fontWeight: "bold",
  },
  question: {
    fontSize: 20,
    marginBottom: 20,
    color: "#555",
  },
  buttonContainer: {
    width: "100%",
    justifyContent: "space-around",
    flexDirection: "row",
    flexWrap: "wrap",
    gap: 10,
  },
  button: {
    width: "40%",
    padding: 15,
    margin: 10,
    borderRadius: 10,
    alignItems: "center",
  },
  happyButton: {
    backgroundColor: "#FFD700",
  },
  sadButton: {
    backgroundColor: "#1E90FF",
  },
  stressedButton: {
    backgroundColor: "#FF6347",
  },
  relaxedButton: {
    backgroundColor: "#32CD32",
  },
  buttonText: {
    fontSize: 18,
    color: "#fff",
    fontWeight: "bold",
  },
});
