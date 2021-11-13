import { Col, Row, Typography } from 'antd';
import { EmptyPageMessage, UserCard } from 'core-ui';
import { useAppSelector } from 'hooks';
import * as React from 'react';
import { User } from 'types';

const { Paragraph } = Typography;

type MentorCardsProps = {
  mentors: User[];
};

export const MentorCards: React.FC<MentorCardsProps> = ({ mentors }) => {
  const { user } = useAppSelector((state) => state.profile);
  const { status } = useAppSelector((state) => state.users);

  if (status === 'pending' || !mentors) {
    return (
      <section className="loading">
        <div className="container">
          <Paragraph type="secondary">Loading mentors..</Paragraph>
        </div>
      </section>
    );
  }

  if (!user.profile && !mentors) {
    return (
      <section className="teacher-listings">
        <div className="container">
          <EmptyPageMessage message="Create profile first to view the list of mentors." />
        </div>
      </section>
    );
  }

  if (mentors.length < 1) {
    return (
      <section className="teacher-listings">
        <div className="container">
          <EmptyPageMessage message="Our algorithm can't find matching mentor for you. Make sure you have enter appropriate information in your profile field." />
        </div>
      </section>
    );
  }

  return (
    <div className="card-lists">
      <Row>
        {mentors.map((mentor) => (
          <Col xs={12} xl={8} key={mentor.username}>
            <UserCard user={mentor} key={mentor.username} />
          </Col>
        ))}
      </Row>
    </div>
  );
};
