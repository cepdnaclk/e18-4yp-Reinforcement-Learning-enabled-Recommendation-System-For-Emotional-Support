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

const music_unique = [
  { label: "Alternative", value: "alternative" },
  { label: "Blues", value: "blues" },
  { label: "Dance", value: "dance" },
  { label: "Electro", value: "electro" },
  { label: "Electronic", value: "electronic" },
  { label: "Folk", value: "folk" },
  { label: "Indie", value: "indie" },
  { label: "Metal", value: "metal" },
  { label: "New Age", value: "new-age" },
  { label: "Pop", value: "pop" },
  { label: "Rock", value: "rock" },
  { label: "Soul", value: "soul" },
  { label: "World Music", value: "world-music" },
];

export default function MusicPreferenceForm({ route, navigation }) {
  const { username, email, password } = route.params;
  const [isFocus, setIsFocus] = useState(false);
  const [selectedSadMusic, setSelectedSadMusic] = useState(null);
  const [selectedHappyMusic, setSelectedHappyMusic] = useState(null);
  const [selectedStressedMusic, setSelectedStressedMusic] = useState(null);
  const [selectedRelaxedMusic, setSelectedRelaxedMusic] = useState(null);

  const handleNext = () => {
    navigation.navigate("MoviePreferenceForm", {
      username,
      email,
      password,
      selectedSadMusic,
      selectedHappyMusic,
      selectedStressedMusic,
      selectedRelaxedMusic,
    });
  };

  return (
    <SafeAreaView style={styles.container}>
      {/* <Text style={styles.title}>Music Preferences</Text> */}
      <Image
        style={{ width: 100, height: 100 }}
        source={require("../assets/signup.gif")}
      />
      <View style={styles.dropdownContainer}>
        {/* <Text style={{ fontSize: 10 }}>
          Your most preferred genre of music when you are sad:
        </Text> */}
        <Dropdown
          style={[styles.dropdown, isFocus && { borderColor: "blue" }]}
          placeholderStyle={styles.placeholderStyle}
          selectedTextStyle={styles.selectedTextStyle}
          inputSearchStyle={styles.inputSearchStyle}
          iconStyle={styles.iconStyle}
          data={music_unique}
          search
          maxHeight={300}
          labelField="label"
          valueField="value"
          placeholder={
            !isFocus
              ? "Your most preferred genre of music when you are sad"
              : "..."
          }
          searchPlaceholder="Search..."
          value={selectedSadMusic}
          onFocus={() => setIsFocus(true)}
          onBlur={() => setIsFocus(false)}
          onChange={(item) => {
            setSelectedSadMusic(item.value);
            setIsFocus(false);
          }}
          renderLeftIcon={() => (
            <AntDesign
              style={styles.icon}
              color={isFocus ? "blue" : "black"}
              name="customerservice"
              size={20}
            />
          )}
        />

        {/* <Text>Your most preferred genre of music when you are happy:</Text> */}
        <Dropdown
          style={[styles.dropdown, isFocus && { borderColor: "blue" }]}
          placeholderStyle={styles.placeholderStyle}
          selectedTextStyle={styles.selectedTextStyle}
          inputSearchStyle={styles.inputSearchStyle}
          iconStyle={styles.iconStyle}
          data={music_unique}
          search
          maxHeight={300}
          labelField="label"
          valueField="value"
          placeholder={
            !isFocus
              ? "Your most preferred genre of music when you are happy"
              : "..."
          }
          searchPlaceholder="Search..."
          value={selectedHappyMusic}
          onFocus={() => setIsFocus(true)}
          onBlur={() => setIsFocus(false)}
          onChange={(item) => {
            setSelectedHappyMusic(item.value);
            setIsFocus(false);
          }}
          renderLeftIcon={() => (
            <AntDesign
              style={styles.icon}
              color={isFocus ? "blue" : "black"}
              name="customerservice"
              size={20}
            />
          )}
        />

        {/* <Text>Your most preferred genre of music when you are stressed:</Text> */}
        <Dropdown
          style={[styles.dropdown, isFocus && { borderColor: "blue" }]}
          placeholderStyle={styles.placeholderStyle}
          selectedTextStyle={styles.selectedTextStyle}
          inputSearchStyle={styles.inputSearchStyle}
          iconStyle={styles.iconStyle}
          data={music_unique}
          search
          maxHeight={300}
          labelField="label"
          valueField="value"
          placeholder={
            !isFocus
              ? "Your most preferred genre of music when you are stressed"
              : "..."
          }
          searchPlaceholder="Search..."
          value={selectedStressedMusic}
          onFocus={() => setIsFocus(true)}
          onBlur={() => setIsFocus(false)}
          onChange={(item) => {
            setSelectedStressedMusic(item.value);
            setIsFocus(false);
          }}
          renderLeftIcon={() => (
            <AntDesign
              style={styles.icon}
              color={isFocus ? "blue" : "black"}
              name="customerservice"
              size={20}
            />
          )}
        />

        {/* <Text>Your most preferred genre of music when you are relaxed:</Text> */}
        <Dropdown
          style={[styles.dropdown, isFocus && { borderColor: "blue" }]}
          placeholderStyle={styles.placeholderStyle}
          selectedTextStyle={styles.selectedTextStyle}
          inputSearchStyle={styles.inputSearchStyle}
          iconStyle={styles.iconStyle}
          data={music_unique}
          search
          maxHeight={300}
          labelField="label"
          valueField="value"
          placeholder={
            !isFocus
              ? "Your most preferred genre of music when you are relaxed"
              : "..."
          }
          searchPlaceholder="Search..."
          value={selectedRelaxedMusic}
          onFocus={() => setIsFocus(true)}
          onBlur={() => setIsFocus(false)}
          onChange={(item) => {
            setSelectedRelaxedMusic(item.value);
            setIsFocus(false);
          }}
          renderLeftIcon={() => (
            <AntDesign
              style={styles.icon}
              color={isFocus ? "blue" : "black"}
              name="customerservice"
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
    paddingBottom: 20,
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
