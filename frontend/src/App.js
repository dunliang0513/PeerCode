import "./css/App.scss";
import Dashboard from "./pages/Dashboard";
import Header from "./components/common/Header";
import { ThemeProvider, createTheme } from "@mui/material/styles";
import { green, orange, red } from "@mui/material/colors";
import "ag-grid-enterprise";
import { QuestionProvider } from "./contexts/QuestionContext";
import ProblemPage from "./pages/Problem";
import { BrowserRouter as Router } from "react-router-dom";
import { Route, Routes } from "react-router-dom";
import Profile from "./pages/Profile";
import Homepage from "./pages/Homepage";
import Login from "./pages/Login";
import SignUp from "./pages/SignUp";
import HomeHeader from "./components/common/HomeHeader";

const theme = createTheme({
  palette: {
    primary: {
      main: "#868686",
      contrastText: "#fff",
    },
    secondary: {
      main: "#333333",
      contrastText: "#fff",
    },
    question_easy: {
      light: green[300],
      dark: green[800],
      contrastText: "#fff",
      main: "#20900D",
    },
    question_medium: {
      light: orange[300],
      dark: orange[800],
      contrastText: "#fff",
      main: orange[500],
    },
    question_hard: {
      light: red[300],
      dark: red[800],
      contrastText: "#fff",
      main: "#E70000",
    },
    question_OTD: {
      main: "#9747FF",
      light: "#A45EFF",
      dark: "#7B16FF",
      contrastText: "#fff",
    },
  },
});

function App() {
  return (
    <Router>
      <ThemeProvider theme={theme}>
        <QuestionProvider>
          <Header />
          <Routes>
            
            <Route exact path="/" element={<SignUp /> } />
            <Route exact path="/" element={<Login /> } /> 
            <Route exact path="/" element={<Dashboard /> } />

            <Route exact path="/" element={
        
                <Homepage />
        
            } />

            <Route exact path="/signup" element={
              <HomeHeader>
                <SignUp />
              </HomeHeader>
            } /> 

            <Route exact path="/login" element={
              <HomeHeader>
                <Login />
              </HomeHeader>
            } />

            <Route exact path="/problem" element={
              <Header>
                <ProblemPage />
              </Header>
            } />
            <Route exact path="/profile" element={
              <Header>
                <Profile />
              </Header>
            } />
          </Routes>
        </QuestionProvider>
      </ThemeProvider>
    </Router>
  );
}

export default App;
