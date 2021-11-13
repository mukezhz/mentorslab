import { Layout } from 'antd';
import { useEffect } from 'react';
import { ErrorBoundary } from 'views/ErrorBoundary';
import { store } from 'store';
import { loadCurrentUser } from './store/auth/auth.actions';
import { Router } from 'router/Router';
import { AppHeader } from 'views';
import 'styles/index.css';

const App = () => {
  useEffect(() => {
    store.dispatch(loadCurrentUser());
  }, []);

  return (
    <ErrorBoundary>
      <Layout id="app">
        <AppHeader />
        <Router />
      </Layout>
    </ErrorBoundary>
  );
};

export default App;
