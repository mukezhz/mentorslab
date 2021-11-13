/**
 * Application wide configuration.
 * The object are nested on basis of redux store
 */
const config = {
  env: process.env.NODE_ENV,
  // baseURI: '/api', // http://localhost:8000/api since we config proxy = 8000
  baseURI: process.env.REACT_APP_URL, // http://localhost:8000/api since we config proxy = 8000
  sentryDSN: process.env.REACT_APP_SENTRY_DSN,
  endpoints: {
    auth: {
      login: '/login/',
      createAccount: '/register/',
      logout: '/logout/',
      me: '/users/me/',
      profile: '/users/',
    },
    users: {
      fetchMentors: '/users/mentors/',
      fetchMentees: '/users/mentees/',
    },
    profile: {
      fetchProfile: '/users',
      createProfile: '/users/create-profile/',
    },
    mentorship: {
      sendMentorshipRequest: '/mentorships/apply/',
      fetchMentorshipRequestsByStudent: '/mentorships/mentee-requests/',
      fetchMentorshipRequestByStudent: '/mentorships/requests/',
      fetchMentorshipRequestsOfMentor: '/mentorships/mentor-requests/',
      fetchMentorshipRequestOfMentor: '/mentorships/requests/',
      updateMentorshipRequestStatus: '/mentorships/update-status/',
      createMentorshipResponse: '/mentorships/response/',
    },
  },
};
export default config;
