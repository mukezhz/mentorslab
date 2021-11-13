import { StatusTag } from 'core-ui';
import moment from 'moment';
import { MentorshipRequest } from 'types';
import { Link } from 'react-router-dom';

type MentorshipRequestDetailsProps = {
  request: MentorshipRequest;
};

export const TeacherMentorshipRequestDetails: React.FC<MentorshipRequestDetailsProps> = ({ request }) => {
  if (!request.mentor_id || !request.mentee_id) {
    return <p>Loading mentor and mentee...</p>;
  }

  return (
    <table>
      <tbody>
        <tr>
          <th>Title</th>
          <td>{request.title}</td>
        </tr>
        <tr>
          <th>Background</th>
          <td>{request.background}</td>
        </tr>
        <tr>
          <th>Expectations</th>
          <td>{request.expectation}</td>
        </tr>
        <tr>
          <th>Message</th>
          <td>{request.message}</td>
        </tr>
        <tr>
          <th>Status</th>
          <td>
            <StatusTag status={request.status} />
          </td>
        </tr>
        <tr>
          <th>Submision Date</th>
          <td>{moment(request.createdAt).format('MMMM Do YYYY, h:mm a')}</td>
        </tr>
        <tr>
          <th>Mentor</th>
          <td>
            <Link to={`/users/${request.mentor_id}`}>{request.mentor_id} (Me)</Link>
          </td>
        </tr>
        <tr>
          <th>Mentee</th>
          <td>
            <Link to={`/users/${request.mentee_id}`}>{request.mentee_id} </Link>
          </td>
        </tr>
      </tbody>
    </table>
  );
};
