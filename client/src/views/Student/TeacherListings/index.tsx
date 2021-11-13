import { Switch, Typography } from 'antd';
import { EmptyPageMessage } from 'core-ui';
import { useAppDispatch, useAppSelector } from 'hooks';
import * as React from 'react';
import { Helmet } from 'react-helmet-async';
import { fetchMentors } from 'store/users/users.action';
import { MentorCards } from './components';

const { Paragraph } = Typography;
export const TeacherListings = () => {
  const dispatch = useAppDispatch();
  const { user } = useAppSelector((state) => state.profile);
  const { user: authUser } = useAppSelector((state) => state.auth);

  const { mentors, status } = useAppSelector((state) => state.users);

  React.useEffect(() => {
    dispatch(fetchMentors());
  }, []);

  if (!user.profile && !authUser.profile) {
    return (
      <section className="teacher-listings">
        <Helmet>
          <title>Teacher Listings | Mentor Labs</title>
        </Helmet>
        <div className="container">
          <EmptyPageMessage message="Please create your profile to view the list of mentors." />
        </div>
      </section>
    );
  }

  return (
    <section className="teacher-listings">
      <Helmet>
        <title>Teacher Listings | Mentor Labs</title>
      </Helmet>
      <div className="container">
        <Paragraph type="secondary" className="text--center">
          List of Mentors
        </Paragraph>
        <MentorCards mentors={mentors} />
      </div>
    </section>
  );
};
