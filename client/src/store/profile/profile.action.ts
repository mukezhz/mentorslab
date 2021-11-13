import { createAsyncThunk } from '@reduxjs/toolkit';
import config from 'config';
import { CreateProfileData, ProfileResponse, User } from 'types';
import http from 'utils/http';

export const fetchProfile = createAsyncThunk('profile/fetchProfile', async (username: string, thunkAPI) => {
  try {
    const url = `${config.endpoints.profile.fetchProfile}/${username}/`;
    const { data: {profile} } = await http.get<User>(url);
    return profile;
  } catch (err) {
    return thunkAPI.rejectWithValue(err.response.data.message);
  }
});

export const createProfile = createAsyncThunk('profile/createProfile', async (values: CreateProfileData, thunkAPI) => {
  try {
    const url = config.endpoints.profile.createProfile;
    const { statusText } = await http.post<ProfileResponse>(url, values);
    return statusText;
  } catch (err) {
    return thunkAPI.rejectWithValue(err.response.data.message);
  }
});
