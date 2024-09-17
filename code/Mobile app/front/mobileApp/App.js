import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";
import LoginForm from "./Login/LoginForm";
import Signup from "./Login/Signup";
import MusicPreferenceForm from "./Login/MusicPreferenceForm";
import MoviePreferenceForm from "./Login/MoviePreferenceForm";
import BookPreferenceForm from "./Login/BookPreferenceForm";
import Home from "./Home";
import Suggestion from "./Suggestion";

const Stack = createStackNavigator();

function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Login">
        <Stack.Screen name="Login" component={LoginForm} />
        <Stack.Screen
          name="Signup"
          component={Signup}
          options={{ headerTitle: "" }}
        />
        <Stack.Screen
          name="MusicPreferenceForm"
          component={MusicPreferenceForm}
          options={{ headerTitle: "Music Preferences" }}
        />
        <Stack.Screen
          name="MoviePreferenceForm"
          component={MoviePreferenceForm}
          options={{ headerTitle: "Movies Preferences" }}
        />
        <Stack.Screen
          name="BookPreferenceForm"
          component={BookPreferenceForm}
          options={{ headerTitle: "Books Preferences" }}
        />
        <Stack.Screen name="Home" component={Home} />
        <Stack.Screen
          name="Suggestion"
          component={Suggestion}
          options={{ headerTitle: "Suggestion" }}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

export default App;
