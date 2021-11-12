import { combineReducers } from '@reduxjs/toolkit';
import authReducer from './auth/auth.slice';
import usersReducer from './users/users.slice';
import profileReducer from './profile/profile.slice';
import mentorshipReducer from './mentorship/mentorship.slice';

const rootReducer = combineReducers({
  auth: authReducer,
  users: usersReducer,
  profile: profileReducer,
  mentorship: mentorshipReducer,
});

export default rootReducer;
