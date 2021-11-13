import { Avatar, Button, Card, Col, Row, Space, Typography } from 'antd';
import { StatusTag } from 'core-ui';
import moment from 'moment';
import { Link, useNavigate } from 'react-router-dom';
import { MentorshipRequest } from 'types';
import http from 'utils/http';
import { User } from 'types';
import { fetchProfile } from 'store/profile/profile.action';
import { useAppDispatch, useAppSelector } from 'hooks';
import * as React from 'react';

type MentorshipRequestCardProps = {
  request: MentorshipRequest;
  loading: boolean;
};

const { Title, Paragraph } = Typography;

export const MentorshipRequestCard: React.FC<MentorshipRequestCardProps> = ({ request, loading }) => {
  const dispatch = useAppDispatch()
  const { user } = useAppSelector((state) => state.profile);
  const navigate = useNavigate();

  React.useEffect(() => {
    dispatch(fetchProfile(request.mentee_id)) 
    // const {data} = await http.get<{user: User}>(`/users/${request.mentee_id}/`)
  }, [])
  const url = `/mentee-requests/${request.uuid}`

  if (!request || !user) {
    return <p>Loading user...</p>;
  }


  return (
    <Card className="mentorship-request-card" loading={loading}>
      <Row justify="space-between">
        <Col>
          <Space size="middle" className="mentorship-request-card__user">
            <Avatar size={65} src={user.avatar} />
            <div>
              <Link to={`/users/${request.mentee_id}`}>
                <b>{request.mentee_id}</b>
              </Link>
              <p>{moment(request.createdAt).startOf('millisecond').fromNow()}</p>
            </div>
          </Space>
        </Col>

        <Col>
          <StatusTag status={request.status} />
        </Col>
      </Row>
      <Link to={url}>
        <Title level={5} className="mt-1">
          {request.title}
        </Title>
      </Link>
      <div className="mentorship-request-card__message">
        <Paragraph ellipsis={{ rows: 3 }}>{request.message}</Paragraph>
      </div>
      <Button type="primary" onClick={() => navigate(url)}>
        View full details
      </Button>
    </Card>
  );
};
