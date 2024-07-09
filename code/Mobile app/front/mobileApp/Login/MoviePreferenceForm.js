import React, { useState } from "react";
import {
  View,
  StyleSheet,
  SafeAreaView,
  Text,
  Pressable,
  Image,
} from "react-native";
import { Dropdown } from "react-native-element-dropdown";
import AntDesign from "@expo/vector-icons/AntDesign";

const movie_unique = [
  { label: "Adventure", value: "Adventure" },
  { label: "Animation", value: "Animation" },
  { label: "Children", value: "Children" },
  { label: "Comedy", value: "Comedy" },
  { label: "Fantasy", value: "Fantasy" },
  { label: "Romance", value: "Romance" },
  { label: "Horror", value: "Horror" },
  { label: "Sci-Fi", value: "Sci-Fi" },
  { label: "Western", value: "Western" },
];

export default function MoviePreferenceForm({ route, navigation }) {
  const {
    username,
    email,
    password,
    selectedSadMusic,
    selectedHappyMusic,
    selectedStressedMusic,
    selectedRelaxedMusic,
  } = route.params;
  const [isFocus, setIsFocus] = useState(false);
  const [selectedSadMovie, setSelectedSadMovie] = useState(null);
  const [selectedHappyMovie, setSelectedHappyMovie] = useState(null);
  const [selectedStressedMovie, setSelectedStressedMovie] = useState(null);
  const [selectedRelaxedMovie, setSelectedRelaxedMovie] = useState(null);

  const handleNext = () => {
    navigation.navigate("BookPreferenceForm", {
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
    });
  };

  return (
    <SafeAreaView style={styles.container}>
      {/* <Text style={styles.title}>Movie Preferences</Text> */}
      <Image
        style={{ width: 100, height: 100 }}
        source={require("../assets/signup.gif")}
      />
      <View style={styles.dropdownContainer}>
        {/* <Text>Your most preferred genre of movie when you are sad:</Text> */}
        <Dropdown
          style={[styles.dropdown, isFocus && { borderColor: "blue" }]}
          placeholderStyle={styles.placeholderStyle}
          selectedTextStyle={styles.selectedTextStyle}
          inputSearchStyle={styles.inputSearchStyle}
          iconStyle={styles.iconStyle}
          data={movie_unique}
          search
          maxHeight={300}
          labelField="label"
          valueField="value"
          placeholder={
            !isFocus
              ? "Your most preferred genre of movie when you are sad"
              : "..."
          }
          searchPlaceholder="Search..."
          value={selectedSadMovie}
          onFocus={() => setIsFocus(true)}
          onBlur={() => setIsFocus(false)}
          onChange={(item) => {
            setSelectedSadMovie(item.value);
            setIsFocus(false);
          }}
          renderLeftIcon={() => (
            <AntDesign
              style={styles.icon}
              color={isFocus ? "blue" : "black"}
              name="videocamera"
              size={20}
            />
          )}
        />

        {/* <Text>Your most preferred genre of movie when you are happy:</Text> */}
        <Dropdown
          style={[styles.dropdown, isFocus && { borderColor: "blue" }]}
          placeholderStyle={styles.placeholderStyle}
          selectedTextStyle={styles.selectedTextStyle}
          inputSearchStyle={styles.inputSearchStyle}
          iconStyle={styles.iconStyle}
          data={movie_unique}
          search
          maxHeight={300}
          labelField="label"
          valueField="value"
          placeholder={
            !isFocus
              ? "Your most preferred genre of movie when you are happy"
              : "..."
          }
          searchPlaceholder="Search..."
          value={selectedHappyMovie}
          onFocus={() => setIsFocus(true)}
          onBlur={() => setIsFocus(false)}
          onChange={(item) => {
            setSelectedHappyMovie(item.value);
            setIsFocus(false);
          }}
          renderLeftIcon={() => (
            <AntDesign
              style={styles.icon}
              color={isFocus ? "blue" : "black"}
              name="videocamera"
              size={20}
            />
          )}
        />

        {/* <Text>Your most preferred genre of movie when you are stressed:</Text> */}
        <Dropdown
          style={[styles.dropdown, isFocus && { borderColor: "blue" }]}
          placeholderStyle={styles.placeholderStyle}
          selectedTextStyle={styles.selectedTextStyle}
          inputSearchStyle={styles.inputSearchStyle}
          iconStyle={styles.iconStyle}
          data={movie_unique}
          search
          maxHeight={300}
          labelField="label"
          valueField="value"
          placeholder={
            !isFocus
              ? "Your most preferred genre of movie when you are stressed"
              : "..."
          }
          searchPlaceholder="Search..."
          value={selectedStressedMovie}
          onFocus={() => setIsFocus(true)}
          onBlur={() => setIsFocus(false)}
          onChange={(item) => {
            setSelectedStressedMovie(item.value);
            setIsFocus(false);
          }}
          renderLeftIcon={() => (
            <AntDesign
              style={styles.icon}
              color={isFocus ? "blue" : "black"}
              name="videocamera"
              size={20}
            />
          )}
        />

        {/* <Text>Your most preferred genre of movie when you are relaxed:</Text> */}
        <Dropdown
          style={[styles.dropdown, isFocus && { borderColor: "blue" }]}
          placeholderStyle={styles.placeholderStyle}
          selectedTextStyle={styles.selectedTextStyle}
          inputSearchStyle={styles.inputSearchStyle}
          iconStyle={styles.iconStyle}
          data={movie_unique}
          search
          maxHeight={300}
          labelField="label"
          valueField="value"
          placeholder={
            !isFocus
              ? "Your most preferred genre of movie when you are relaxed"
              : "..."
          }
          searchPlaceholder="Search..."
          value={selectedRelaxedMovie}
          onFocus={() => setIsFocus(true)}
          onBlur={() => setIsFocus(false)}
          onChange={(item) => {
            setSelectedRelaxedMovie(item.value);
            setIsFocus(false);
          }}
          renderLeftIcon={() => (
            <AntDesign
              style={styles.icon}
              color={isFocus ? "blue" : "black"}
              name="videocamera"
              size={20}
            />
          )}
        />
      </View>

      <View style={styles.buttonView}>
        <Pressable style={styles.button} onPress={handleNext}>
          <Text style={styles.buttonText}>Next</Text>
        </Pressable>
      </View>
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
});
