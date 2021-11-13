import { Button, Form, Input, Select, Space, Typography } from 'antd';
import { countries, languages, socials } from 'data';
import { tags } from 'data/tags';
import { useAppDispatch, useAppSelector } from 'hooks';
import * as React from 'react';
import { AiOutlineMinusCircle, AiOutlinePlus } from 'react-icons/ai';
import { createProfile, fetchProfile } from 'store/profile/profile.action';
import { CreateProfileData } from 'types';
import { displayErrorMessage, displaySuccessNotification } from 'utils/notifications';
import { User } from 'types';

const { Item, List } = Form;
const { Title, Text } = Typography;
const { Option } = Select;

type UserProfileProps = {
  user: User;
};

export const ProfileCreate: React.FC<UserProfileProps> = ({user}) => {
  const dispatch = useAppDispatch();
  const { status, error } = useAppSelector(state => state.profile);

  React.useEffect(() => {
    if (status === 'rejected' && error) {
      dispatch(fetchProfile(user.username));
      displayErrorMessage(error);
      return;
    }
  }, [status, error]);

  const onFormSubmit = (values: CreateProfileData) => {
    dispatch(createProfile(values)).then((value: any) => {
        if (!value.error){
          displaySuccessNotification(`Your profile has been created!!!`)
        }
    })
  };

  const onFinishFailed = () => {
    displayErrorMessage('Please complete all required form fields!');
    return;
  };

  return (
    <div className="profile-create">
      <div className="container">
        <Form layout="vertical" onFinish={onFormSubmit} onFinishFailed={onFinishFailed} size="large">
          <div className="profile-create__form-header">
            <Title level={3} className="profile-create__form-title">
              Hi! Let's get started filling your profile information.
            </Title>
            <Text type="secondary">
              In this form, we'll collect some basic and additional information about you. Your data is feed in our
              algorithm to recommend other users, so make sure that information entered is correct. 👇
            </Text>
          </div>

          {/* title start */}
          <Item
            label="Title"
            name="title"
            rules={[{ required: true, message: 'Please enter what defines your title!' }]}
          >
            <Input placeholder="Software Engineer" />
          </Item>
          {/* title start */}

          {/* description start */}
          <Item
            label="Description"
            extra="Max character count of 400"
            name="description"
            rules={[
              {
                required: true,
                message: 'Please describe about you in short!',
              },
              {
                min: 100,
                message: 'Minimum length should be 100 characters!',
              },
            ]}
          >
            <Input.TextArea
              rows={3}
              maxLength={400}
              placeholder="Software engineer with 10+ years of experience in Machine Learning, Cloud Computing and BlockChain."
            />
          </Item>
          {/* description end */}

          {/* countries start */}
          <Item
            label="Country"
            name="country"
            rules={[
              {
                required: true,
                message: 'Please enter a country you are from!',
              },
            ]}
          >
            <Select showSearch placeholder="Select a country">
              {countries.map((country, index) => (
                <Option value={country} key={index}>
                  {country}
                </Option>
              ))}
            </Select>
          </Item>
          {/* countries end */}

          {/* tags start*/}
          <Item
            label="Tags"
            name="tags"
            rules={[
              {
                required: true,
                message: 'Enter 3 to 5 tags!',
                type: 'array',
                min: 3,
                max: 5,
              },
            ]}
          >
            <Select
              mode="tags"
              style={{ width: '100%' }}
              tokenSeparators={[',']}
              placeholder="Start typing tags you specialize on"
            >
              {tags.map((tag) => (
                <Option key={tag} value={tag}>
                  {tag}
                </Option>
              ))}
            </Select>
          </Item>
          {/* tags end */}

          {/* languages start */}
          <Item
            label="Languages"
            name="languages"
            rules={[
              {
                required: true,
                message: 'Enter 2 to 5 languages!',
                type: 'array',
                min: 2,
                max: 5,
              },
            ]}
          >
            <Select
              mode="multiple"
              allowClear
              style={{ width: '100%' }}
              placeholder="Please select languages you can speak"
              // defaultValue={['English']}
            >
              {languages.map((lang) => (
                <Option key={lang.code} value={lang.name}>
                  {lang.name}
                </Option>
              ))}
            </Select>
          </Item>
          {/* languages end */}
          <Item>
            <Button type="primary" htmlType="submit">
              Submit
            </Button>
          </Item>
        </Form>
      </div>
    </div>
  );
};
