import { GlobalStyle } from './styles/global';
import { Dashboard } from './components/Dashboard';
import {Header} from './components/Header/header';


function App() {
  return (
    <>
      <Header/>
      <Dashboard />
      <GlobalStyle />
    </>
  );
}

export default App;