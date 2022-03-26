import { GlobalStyle } from './styles/global';
import { Dashboard } from './components/Dashboard';
import {Header} from './components/Header/header';
import { useState } from 'react'
import Modal from 'react-modal';
import { NewTransactionModal } from './components/Modals';

Modal.setAppElement('#root');

function App() {

  const [isNewTransactionModalOpen, setisNewTransactionModalOpen] = useState(false);

  function handleOpenNewTransactionModal(){
      setisNewTransactionModalOpen(true);
  }

  function handleCloseNewTransactionModal(){
      setisNewTransactionModalOpen(false);
  }

  return (
    <>
      <Header onOpenNewTransactionModal={handleOpenNewTransactionModal}/>
      <Dashboard />
      <NewTransactionModal isOpen={isNewTransactionModalOpen} onRequestClose={handleCloseNewTransactionModal}></NewTransactionModal>
      <GlobalStyle />

    </>
  );
}

export default App;