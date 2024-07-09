import React, { useState } from "react";
import {
  Alert,
  Image,
  Pressable,
  SafeAreaView,
  StyleSheet,
  Switch,
  Text,
  TextInput,
  View,
  ActivityIndicator,
} from "react-native";
const logo = require("../assets/logo/logo.png");

export default function LoginForm({ navigation }) {
  const [click, setClick] = useState(false);
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);

  const handleLogin = () => {
    setLoading(true);
    fetch("http://10.0.2.2:5000/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username,
        password,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        setLoading(false);
        if (data.message === "Login successful") {
          Alert.alert("Login Successful");
          navigation.navigate("Home", {
            username: data.username,
            userid: data.userid,
          }); // Navigate to Home page
        } else {
          Alert.alert("Invalid username or password");
        }
      })
      .catch((error) => {
        setLoading(false);
        console.error("Error:", error);
        Alert.alert("An error occurred during login");
      });
  };

  return (
    <SafeAreaView style={styles.container}>
      <Image source={logo} style={styles.image} resizeMode="contain" />
      <Text style={styles.title}>Ascend</Text>
      <View style={styles.inputView}>
        <TextInput
          style={styles.input}
          placeholder="EMAIL OR USERNAME"
          value={username}
          onChangeText={setUsername}
          autoCorrect={false}
          autoCapitalize="none"
        />
        <TextInput
          style={styles.input}
          placeholder="PASSWORD"
          secureTextEntry
          value={password}
          onChangeText={setPassword}
          autoCorrect={false}
          autoCapitalize="none"
        />
      </View>
      <View style={styles.rememberView}>
        <View style={styles.switch}>
          <Switch
            value={click}
            onValueChange={setClick}
            trackColor={{ true: "green", false: "gray" }}
          />
          <Text style={styles.rememberText}>Remember Me</Text>
        </View>
        <View>
          <Pressable onPress={() => Alert.alert("Forget Password!")}>
            <Text style={styles.forgetText}>Forgot Password?</Text>
          </Pressable>
        </View>
      </View>

      {loading ? (
        <View style={styles.loadingContainer}>
          <ActivityIndicator size="large" color="red" />
          <Text style={styles.loadingText}>Logging in, please wait...</Text>
        </View>
      ) : (
        <View style={styles.buttonView}>
          <Pressable style={styles.button} onPress={handleLogin}>
            <Text style={styles.buttonText}>LOGIN</Text>
          </Pressable>
          <Text style={styles.optionsText}> </Text>
        </View>
      )}

      <Text style={styles.footerText}>
        Don't Have Account?{" "}
        <Text
          style={styles.signup}
          onPress={() => navigation.navigate("Signup")}
        >
          Sign Up
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
  image: {
    height: 160,
    width: 170,
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
  rememberView: {
    width: "100%",
    paddingHorizontal: 50,
    justifyContent: "space-between",
    alignItems: "center",
    flexDirection: "row",
    marginBottom: 8,
  },
  switch: {
    flexDirection: "row",
    gap: 1,
    justifyContent: "center",
    alignItems: "center",
  },
  rememberText: {
    fontSize: 13,
  },
  forgetText: {
    fontSize: 11,
    color: "red",
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
    paddingHorizontal: 50,
  },
  optionsText: {
    textAlign: "center",
    paddingVertical: 10,
    color: "gray",
    fontSize: 13,
    marginBottom: 6,
  },
  footerText: {
    textAlign: "center",
    color: "gray",
  },
  signup: {
    color: "red",
    fontSize: 13,
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
