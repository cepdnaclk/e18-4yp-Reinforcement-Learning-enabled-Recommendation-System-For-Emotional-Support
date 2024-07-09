import React, { useState } from "react";
import {
  View,
  TextInput,
  Button,
  StyleSheet,
  SafeAreaView,
  Text,
  Pressable,
  Alert, Image,
} from "react-native";


// Main Component
export default function Signup({ navigation }) {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
 

  const handleNext = () => {
    navigation.navigate("MusicPreferenceForm", { username, email, password });
  };

  return (
    <SafeAreaView style={styles.container}>
      <Image
        style={{ width: 100, height: 100 }}
        source={require("../assets/signup.gif")}
        />
      <Text style={styles.title}>Sign Up</Text>
      <View style={styles.inputView}>
        <TextInput
          style={styles.input}
          placeholder="Username"
          value={username}
          onChangeText={setUsername}
        />
        <TextInput
          style={styles.input}
          placeholder="Email"
          value={email}
          onChangeText={setEmail}
          keyboardType="email-address"
        />
        <TextInput
          style={styles.input}
          placeholder="Password"
          value={password}
          onChangeText={setPassword}
          secureTextEntry
        />
      </View>

      <View style={styles.buttonView}>
        <Pressable style={styles.button} onPress={handleNext}>
          <Text style={styles.buttonText}>Next</Text>
        </Pressable>
      </View>
      <Text style={styles.footerText}>
        Already Have Account?{" "}
        <Text
          style={styles.signup}
          onPress={() => navigation.navigate("Login")}
        >
          Login
        </Text>
      </Text>
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
  inputView: {
    gap: 15,
    width: "100%",
    paddingHorizontal: 40,
    marginBottom: 5,
  },
  input: {
    height: 50,
    paddingHorizontal: 20,
    borderColor: "red",
    borderWidth: 1,
    borderRadius: 7,
  },
  dropdownContainer: {
    width: "100%",
    paddingHorizontal: 40,
    marginTop: 20,
  },
  dropdown: {
    height: 50,
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
  footerText: {
    textAlign: "center",
    color: "gray",
  },
  signup: {
    color: "red",
    fontSize: 13,
  },
});
