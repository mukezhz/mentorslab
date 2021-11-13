import { createAsyncThunk } from "@reduxjs/toolkit";
import config from "config";
import { CreateAccountData, LoginData, Profile, User, Auth } from "types";
import http from "utils/http";

export const loadCurrentUser = createAsyncThunk(
  "auth/loadCurrentUser",
  async (_, thunkAPI) => {
    try {
      const user = localStorage.getItem('user')
      if (user != null) {
        return {}
      } 
      const url = config.endpoints.auth.me;
      const { data } = await http.get<{ user: User }>(url);
      console.log(data)
      localStorage.setItem("user", JSON.stringify(data))
      return data;
    } catch (err) {
      return thunkAPI.rejectWithValue(err.response.data.detail);
    }
  }
);

export const loadCurrentUserProfile = createAsyncThunk(
  "auth/loadCurrentUserProfile",
  async (username, thunkAPI) => {
    try {
      const url = config.endpoints.auth.profile;
      const { data } = await http.get<User>(`${url}/${username}/`);
      return data.profile;
    } catch (err) {
      return thunkAPI.rejectWithValue(err.response.data.detail);
    }
  }
);

export const createAccount = createAsyncThunk(
  "auth/createAccount",
  async ({ first_name, last_name, username, email, password, password2, role }: CreateAccountData, thunkAPI) => {
    try {
      const url = config.endpoints.auth.createAccount;
      const { data } = await http.post<{ user: User }>(url, { first_name, last_name, username, email, password, password2, role });
      return data;
    } catch (err) {
      // console.log(err.response.data);
      const errors = err.response.data
      const { 0:errs } = Object.keys(errors).map(err => errors[err].map(d=>d))
      return thunkAPI.rejectWithValue(Object.keys(errors)[0]+ " " + errs[0]);
    }
  }
);

export const logIn = createAsyncThunk(
  "auth/logIn",
  async ({ email, password }: LoginData, thunkAPI) => {
    try {
      const url = config.endpoints.auth.login;
      const {data: { access }} = await http.post<{ access: Auth }>(url, { email, password });
      const me = config.endpoints.auth.me;
      const { data } = await http.get<{ user: User }>(me, {
        headers:{
          "Content-Type": "application/json",
          "Authorization": "Jwt " + access as string
        }
      });
      localStorage.setItem("user", JSON.stringify(data))
      localStorage.setItem("access_token", access as string);
      return access;
    } catch (err) {
      return thunkAPI.rejectWithValue(err.response.data.message);
    }
  }
);

export const logOut = createAsyncThunk("auth/logOut", async (_, thunkAPI) => {
  try {
    // const url = config.endpoints.auth.logout;
    localStorage.removeItem("user");
    localStorage.removeItem("access_token");
    // await http.post(url);
  } catch (err) {
    return thunkAPI.rejectWithValue("Error in logout");
  }
});
