import React, { useState } from "react";
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  FlatList,
  Alert,
  ActivityIndicator,
} from "react-native";
import Icon from "react-native-vector-icons/MaterialIcons";

export default function Suggestions({ route, navigation }) {
  const { suggestions: initialSuggestions, userid, emotion } = route.params;
  const [suggestions, setSuggestions] = useState(initialSuggestions);
  const [preference, setPreference] = useState(null);
  const [loading, setLoading] = useState(false);
  console.log(userid);
  const handlePreferenceSelect = (selectedPreference) => {
    setPreference(selectedPreference);
  };

  const handleReload = () => {
    setLoading(true);
    fetch(`http://10.0.2.2:5000/get-suggestions`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        userid: userid,
        emotion: emotion,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        setLoading(false);
        if (data.suggestions) {
          setSuggestions(data.suggestions);
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

  const handleSuggestionClick = (suggestion) => {
    console.log("Suggestion clicked:", suggestion);
    fetch(`http://10.0.2.2:5000/update-preference`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        userid: userid,
        suggestion: suggestion,
      }),
    })
      .then((response) => {
        if (response.status === 200) {
          return response.json();
        } else {
          throw new Error("Failed to fetch: " + response.statusText);
        }
      })
      .then((data) => {
        if (data.message === "Preference updated") {
          Alert.alert("Suggestion updated successfully");
        } else {
          Alert.alert("Failed to update suggestion");
        }
      })
      .catch((error) => {
        console.error("Error:", error);
        Alert.alert("An error occurred while updating suggestion");
      });
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Your Most Preferable</Text>
      <View style={styles.buttonContainer}>
        <TouchableOpacity
          style={[
            styles.button,
            preference === "Movies" && styles.selectedButton,
          ]}
          onPress={() => handlePreferenceSelect("Movies")}
        >
          <Icon name="local-movies" size={30} color="#fff" />
          <Text style={styles.buttonText}>Movies</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={[
            styles.button,
            preference === "Music" && styles.selectedButton,
          ]}
          onPress={() => handlePreferenceSelect("Music")}
        >
          <Icon name="music-note" size={30} color="#fff" />
          <Text style={styles.buttonText}>Music</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={[
            styles.button,
            preference === "Books" && styles.selectedButton,
          ]}
          onPress={() => handlePreferenceSelect("Books")}
        >
          <Icon name="book" size={30} color="#fff" />
          <Text style={styles.buttonText}>Books</Text>
        </TouchableOpacity>
      </View>

      {preference && (
        <View style={styles.suggestionsContainer}>
          <Text style={styles.suggestionsTitle}>
            Suggestions for {preference}
          </Text>
          {loading ? (
            <ActivityIndicator size="large" color="red" />
          ) : (
            <FlatList
              data={suggestions[preference.toLowerCase()]}
              keyExtractor={(item, index) => index.toString()}
              renderItem={({ item }) => (
                <TouchableOpacity
                  style={styles.suggestionItem}
                  onPress={() => handleSuggestionClick(item)}
                >
                  <Text style={styles.suggestionText}>{item}</Text>
                </TouchableOpacity>
              )}
            />
          )}
        </View>
      )}

      <TouchableOpacity style={styles.reloadButton} onPress={handleReload}>
        <Icon name="refresh" size={30} color="#fff" />
        <Text style={styles.buttonText}>Reload</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: "#f5f5f5",
  },
  title: {
    fontSize: 24,
    fontWeight: "bold",
    marginBottom: 20,
    textAlign: "center",
  },
  buttonContainer: {
    justifyContent: "center",
    marginBottom: 20,
  },
  button: {
    flexDirection: "row",
    alignItems: "center",
    padding: 15,
    marginBottom: 15,
    borderRadius: 10,
    backgroundColor: "#ddd",
    alignItems: "center",
    justifyContent: "center",
  },
  selectedButton: {
    backgroundColor: "#007BFF",
  },
  buttonText: {
    fontSize: 18,
    color: "#fff",
    fontWeight: "bold",
    marginLeft: 10,
  },
  suggestionsContainer: {
    marginTop: 20,
  },
  suggestionsTitle: {
    fontSize: 20,
    fontWeight: "bold",
    marginBottom: 10,
  },
  suggestionItem: {
    padding: 15,
    marginBottom: 10,
    backgroundColor: "#fff",
    borderRadius: 10,
    shadowColor: "#000",
    shadowOpacity: 0.1,
    shadowRadius: 10,
    shadowOffset: { width: 0, height: 5 },
  },
  suggestionText: {
    fontSize: 18,
  },
  reloadButton: {
    flexDirection: "row",
    alignItems: "center",
    padding: 15,
    marginTop: 15,
    borderRadius: 10,
    backgroundColor: "#007BFF",
    alignItems: "center",
    justifyContent: "center",
  },
});
