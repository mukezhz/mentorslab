import * as routes from "constants/routes";
import { Role } from "enums";
import { Route, Routes } from "react-router-dom";
import {
  CreateAccount,
  Home,
  Login,
  NotFound,
  // Room,
  StudentDashboard,
  StudentMentorshipRequest,
  StudentMentorshipRequests,
  TeacherDashboard,
  TeacherListings,
  TeacherMentorshipRequest,
  TeacherMentorshipRequests,
} from "views";
import { Profile } from "../views/Profile";
import { AuthRoute } from "./AuthRoute";
import { NonAuthRoute } from "./NonAuthRoute";

/**
 * Top level application router
 * @returns {Component}
 */
export const Router = () => {
  return (
    <Routes>
      <Route
        path={routes.HOME}
        element={
          <NonAuthRoute>
            <Home />
          </NonAuthRoute>
        }
      />
      <Route
        path={routes.CREATE_ACCOUNT}
        element={
          <NonAuthRoute>
            <CreateAccount />
          </NonAuthRoute>
        }
      />
      <Route
        path={routes.LOGIN}
        element={
          <NonAuthRoute>
            <Login />
          </NonAuthRoute>
        }
      />
      <Route
        path={routes.USER_PROFILE}
        element={
          <AuthRoute roles={[Role.STUDENT, Role.TEACHER]}>
            <Profile />
          </AuthRoute>
        }
      />
      <Route
        path={routes.TEACHER_DASHBOARD}
        element={
          <AuthRoute roles={[Role.TEACHER]}>
            <TeacherDashboard />
          </AuthRoute>
        }
      />
      <Route
        path={routes.STUDENT_DASHBOARD}
        element={
          <AuthRoute roles={[Role.STUDENT]}>
            <StudentDashboard />
          </AuthRoute>
        }
      />
      <Route
        path={routes.TEACHER_LISTINGS}
        element={
          <AuthRoute roles={[Role.STUDENT]}>
            <TeacherListings />
          </AuthRoute>
        }
      />
      <Route
        path={routes.STUDENT_MENTORSHIP_REQUESTS}
        element={
          <AuthRoute roles={[Role.STUDENT]}>
            <StudentMentorshipRequests />
          </AuthRoute>
        }
      />
      <Route
        path={routes.STUDENT_MENTORSHIP_REQUEST}
        element={
          <AuthRoute roles={[Role.STUDENT]}>
            <StudentMentorshipRequest />
          </AuthRoute>
        }
      />
      <Route
        path={routes.TEACHER_MENTORSHIP_REQUESTS}
        element={
          <AuthRoute roles={[Role.TEACHER]}>
            <TeacherMentorshipRequests />
          </AuthRoute>
        }
      />

      <Route
        path={routes.TEACHER_MENTORSHIP_REQUEST}
        element={
          <AuthRoute roles={[Role.TEACHER]}>
            <TeacherMentorshipRequest />
          </AuthRoute>
        }
      />
      <Route path="*" element={<NotFound />} />
    </Routes>
  );
};
