import { Layout } from 'antd';
import { Link } from 'react-router-dom';
import logo from './assets/logo.svg';
import { MenuItems } from './components';

const { Header } = Layout;

export const AppHeader = () => {
  return (
    <Header className="app-header">
      <div className="app-header__logo">
        <Link to="/">
          <img src={logo} alt="TinyHouse logo" />
        </Link>
      </div>
      <div className="app-header__menu-section">
        <MenuItems />
      </div>
    </Header>
  );
};
