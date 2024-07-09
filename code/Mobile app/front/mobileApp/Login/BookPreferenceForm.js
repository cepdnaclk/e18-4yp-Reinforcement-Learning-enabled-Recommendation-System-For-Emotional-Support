import React, { useState } from "react";
import {
  View,
  StyleSheet,
  SafeAreaView,
  Text,
  Pressable,
  Alert,
  Image,
  ActivityIndicator,
} from "react-native";
import { Dropdown } from "react-native-element-dropdown";
import AntDesign from "@expo/vector-icons/AntDesign";

const books_unique = [
  { label: "Fiction", value: "Fiction" },
  { label: "Classics", value: "Classics" },
  { label: "Science Fiction", value: "Science Fiction" },
  { label: "Historical Fiction", value: "Historical Fiction" },
  { label: "Horror", value: "Horror" },
  { label: "Poetry", value: "Poetry" },
  { label: "Travel", value: "Travel" },
  { label: "Nonfiction", value: "Nonfiction" },
  { label: "Comics", value: "Comics" },
  { label: "Graphic Novels", value: "Graphic Novels" },
  { label: "Young Adult", value: "Young Adult" },
  { label: "Mystery", value: "Mystery" },
  { label: "Crime", value: "Crime" },
  { label: "Thriller", value: "Thriller" },
  { label: "Romance", value: "Romance" },
  { label: "Chick Lit", value: "Chick Lit" },
  { label: "Art", value: "Art" },
  { label: "Music", value: "Music" },
  { label: "Paranormal", value: "Paranormal" },
  { label: "LGBT", value: "LGBT" },
  { label: "Children's", value: "Children's" },
  { label: "Sports", value: "Sports" },
  { label: "Memoir", value: "Memoir" },
  { label: "Biography", value: "Biography" },
  { label: "Religion", value: "Religion" },
  { label: "History", value: "History" },
  { label: "Philosophy", value: "Philosophy" },
  { label: "Self Help", value: "Self Help" },
  { label: "Psychology", value: "Psychology" },
  { label: "Business", value: "Business" },
  { label: "Spirituality", value: "Spirituality" },
  { label: "Humor", value: "Humor" },
  { label: "Science", value: "Science" },
  { label: "Business", value: "Business" },
  { label: "Religion", value: "Religion" },
];

export default function BookPreferenceForm({ route, navigation }) {
  const {
    username,
    email,
    password,
    selectedSadMusic,
    selectedHappyMusic,
    selectedStressedMusic,
    selectedRelaxedMusic,
    selectedSadMovie,
    selectedHappyMovie,
    selectedStressedMovie,
    selectedRelaxedMovie,
  } = route.params;
  const [isFocus, setIsFocus] = useState(false);
  const [selectedSadBook, setSelectedSadBook] = useState(null);
  const [selectedHappyBook, setSelectedHappyBook] = useState(null);
  const [selectedStressedBook, setSelectedStressedBook] = useState(null);
  const [selectedRelaxedBook, setSelectedRelaxedBook] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSignup = () => {
    setLoading(true);
    fetch("http://10.0.2.2:5000/signup", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username,
        email,
        password,
        preferences: {
          music: {
            sad: selectedSadMusic,
            happy: selectedHappyMusic,
            stressed: selectedStressedMusic,
            relaxed: selectedRelaxedMusic,
          },
          movies: {
            sad: selectedSadMovie,
            happy: selectedHappyMovie,
            stressed: selectedStressedMovie,
            relaxed: selectedRelaxedMovie,
          },
          books: {
            sad: selectedSadBook,
            happy: selectedHappyBook,
            stressed: selectedStressedBook,
            relaxed: selectedRelaxedBook,
          },
        },
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        setLoading(false);
        if (data.message === "Signup successful") {
          Alert.alert("Signup Successful");
          navigation.navigate("Login");
        } else {
          Alert.alert("Signup failed");
        }
      })
      .catch((error) => {
        setLoading(false);
        console.error("Error:", error);
        Alert.alert("An error occurred during signup");
      });
  };

  return (
    <SafeAreaView style={styles.container}>
      <Image
        style={{ width: 100, height: 100 }}
        source={require("../assets/signup.gif")}
      />
      <View style={styles.dropdownContainer}>
        <Dropdown
          style={[styles.dropdown, isFocus && { borderColor: "blue" }]}
          placeholderStyle={styles.placeholderStyle}
          selectedTextStyle={styles.selectedTextStyle}
          inputSearchStyle={styles.inputSearchStyle}
          iconStyle={styles.iconStyle}
          data={books_unique}
          search
          maxHeight={300}
          labelField="label"
          valueField="value"
          placeholder={
            !isFocus
              ? "Your most preferred genre of book when you are sad"
              : "..."
          }
          searchPlaceholder="Search..."
          value={selectedSadBook}
          onFocus={() => setIsFocus(true)}
          onBlur={() => setIsFocus(false)}
          onChange={(item) => {
            setSelectedSadBook(item.value);
            setIsFocus(false);
          }}
          renderLeftIcon={() => (
            <AntDesign
              style={styles.icon}
              color={isFocus ? "blue" : "black"}
              name="book"
              size={20}
            />
          )}
        />
        <Dropdown
          style={[styles.dropdown, isFocus && { borderColor: "blue" }]}
          placeholderStyle={styles.placeholderStyle}
          selectedTextStyle={styles.selectedTextStyle}
          inputSearchStyle={styles.inputSearchStyle}
          iconStyle={styles.iconStyle}
          data={books_unique}
          search
          maxHeight={300}
          labelField="label"
          valueField="value"
          placeholder={
            !isFocus
              ? "Your most preferred genre of book when you are happy"
              : "..."
          }
          searchPlaceholder="Search..."
          value={selectedHappyBook}
          onFocus={() => setIsFocus(true)}
          onBlur={() => setIsFocus(false)}
          onChange={(item) => {
            setSelectedHappyBook(item.value);
            setIsFocus(false);
          }}
          renderLeftIcon={() => (
            <AntDesign
              style={styles.icon}
              color={isFocus ? "blue" : "black"}
              name="book"
              size={20}
            />
          )}
        />
        <Dropdown
          style={[styles.dropdown, isFocus && { borderColor: "blue" }]}
          placeholderStyle={styles.placeholderStyle}
          selectedTextStyle={styles.selectedTextStyle}
          inputSearchStyle={styles.inputSearchStyle}
          iconStyle={styles.iconStyle}
          data={books_unique}
          search
          maxHeight={300}
          labelField="label"
          valueField="value"
          placeholder={
            !isFocus
              ? "Your most preferred genre of book when you are stressed"
              : "..."
          }
          searchPlaceholder="Search..."
          value={selectedStressedBook}
          onFocus={() => setIsFocus(true)}
          onBlur={() => setIsFocus(false)}
          onChange={(item) => {
            setSelectedStressedBook(item.value);
            setIsFocus(false);
          }}
          renderLeftIcon={() => (
            <AntDesign
              style={styles.icon}
              color={isFocus ? "blue" : "black"}
              name="book"
              size={20}
            />
          )}
        />
        <Dropdown
          style={[styles.dropdown, isFocus && { borderColor: "blue" }]}
          placeholderStyle={styles.placeholderStyle}
          selectedTextStyle={styles.selectedTextStyle}
          inputSearchStyle={styles.inputSearchStyle}
          iconStyle={styles.iconStyle}
          data={books_unique}
          search
          maxHeight={300}
          labelField="label"
          valueField="value"
          placeholder={
            !isFocus
              ? "Your most preferred genre of book when you are relaxed"
              : "..."
          }
          searchPlaceholder="Search..."
          value={selectedRelaxedBook}
          onFocus={() => setIsFocus(true)}
          onBlur={() => setIsFocus(false)}
          onChange={(item) => {
            setSelectedRelaxedBook(item.value);
            setIsFocus(false);
          }}
          renderLeftIcon={() => (
            <AntDesign
              style={styles.icon}
              color={isFocus ? "blue" : "black"}
              name="book"
              size={20}
            />
          )}
        />
      </View>

      {loading ? (
        <View style={styles.loadingContainer}>
          <ActivityIndicator size="large" color="red" />
          <Text style={styles.loadingText}>Signing up, please wait...</Text>
        </View>
      ) : (
        <View style={styles.buttonView}>
          <Pressable style={styles.button} onPress={handleSignup}>
            <Text style={styles.buttonText}>Complete Signup</Text>
          </Pressable>
        </View>
      )}
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    alignItems: "center",
    paddingTop: 40,
  },
  title: {
    fontSize: 30,
    fontWeight: "bold",
    textTransform: "uppercase",
    textAlign: "center",
    paddingVertical: 20,
    color: "red",
  },
  dropdownContainer: {
    width: "100%",
    paddingHorizontal: 40,
    paddingVertical: 10,
    marginTop: 20,
  },
  dropdown: {
    height: 60,
    borderColor: "red",
    borderWidth: 0.5,
    borderRadius: 8,
    paddingHorizontal: 8,
    marginTop: 10,
  },
  icon: {
    marginRight: 5,
  },
  placeholderStyle: {
    fontSize: 16,
  },
  selectedTextStyle: {
    fontSize: 16,
  },
  iconStyle: {
    width: 20,
    height: 20,
  },
  inputSearchStyle: {
    height: 40,
    fontSize: 16,
  },
  button: {
    backgroundColor: "red",
    height: 45,
    borderColor: "gray",
    borderWidth: 1,
    borderRadius: 5,
    alignItems: "center",
    justifyContent: "center",
  },
  buttonText: {
    color: "white",
    fontSize: 18,
    fontWeight: "bold",
  },
  buttonView: {
    width: "100%",
    paddingHorizontal: 150,
    paddingVertical: 10,
  },
  loadingContainer: {
    alignItems: "center",
    justifyContent: "center",
    marginTop: 20,
  },
  loadingText: {
    marginTop: 10,
    fontSize: 16,
    color: "gray",
  },
});
