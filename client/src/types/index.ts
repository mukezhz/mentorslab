import { Action, ThunkAction } from "@reduxjs/toolkit";
import { MentorshipRequestStatus, Role } from "enums";
import { store } from "store";

//==============================================================================
// Auth
//==============================================================================
export interface Auth {
  access?: string;
}

//==============================================================================
// Form Data
//==============================================================================
export interface CreateAccountData {
  first_name: string;
  last_name: string;
  username: string;
  email: string;
  password: string;
  password2: string;
  role: Role;
}

export interface LoginData {
  email: string;
  password: string;
}

export interface CreateProfileData extends Omit<Profile, "id" | "userId"> {}

export interface MentorshipRequestData {
  title: string;
  background: string;
  expectation: string;
  message: string;
}

export interface MentorshipResponseData {
  date: string;
  startTime: string;
  endTime: string;
  roomId: string;
  message: string;
}

export interface CreateRoomData {
  title: string;
  creatorId: string;
}

export interface JoinRoomData {
  roomId: string;
}
//==============================================================================
// User
//==============================================================================
export interface User {
  id?: string;
  uuid?: string;
  username?: string;
  first_name?: string;
  last_name?: string;
  email?: string;
  avatar?: string;
  role?: Role;
  profile?: Profile;
}

//==============================================================================
// Profile
//==============================================================================
export interface Socials {
  facebook?: string;
  linkedin?: string;
  twitter?: string;
  portfolio?: string;
  slack?: string;
  github?: string;
}

export interface Channel {
  site: keyof Socials;
  link: string;
}

export interface Profile {
  id: string;
  uuid: string;
  title: string;
  description: string;
  tags: string[];
  country: string;
  languages: string[];
  channels: Channel[];
  userId: string;
}

//==============================================================================
// Mentorship request
//==============================================================================
export interface MentorshipRequest extends MentorshipRequestData {
  id: string;
  title: string;
  menteeId: string;
  mentorId: string;
  status: MentorshipRequestStatus;
  mentor: User;
  mentee: User;
  createdAt: Date;
  response?: MentorshipResponseData;
}

//==============================================================================
// State
//==============================================================================

type Status = "idle" | "pending" | "resolved" | "rejected" | "logged";

export interface AuthState {
  status: Status;
  isAuthenticated: boolean;
  error: string;
  access: string;
  user: User;
}

export interface ErrorState {
  message: string | null;
}

export interface UsersState {
  status: Status;
  mentors: User[];
}

export interface ProfileState {
  status: Status;
  user: User;
  error: string;
  msg: string;
}

export interface ProfileResponse {
  msg: string;
  ok: boolean;
}

export interface MentorshipState {
  status: Status;
  requests: MentorshipRequest[];
  request: MentorshipRequest;
  error: string;
}

//==============================================================================
// Redux Utilities data types
//==============================================================================

export type RootState = ReturnType<typeof store.getState>;

export type AppDispatch = typeof store.dispatch;

export type AppThunk = ThunkAction<void, RootState, null, Action<string>>;
