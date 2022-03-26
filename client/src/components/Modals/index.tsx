import { useState, FormEvent } from 'react';
import Modal from 'react-modal';
import { api } from '../../services/api';
import { Container,TransactionTypeContainer,RadioBox } from './styles';

interface NewTransactionModalsProps{
    isOpen: boolean;
    onRequestClose: () => void;
}

export function NewTransactionModal({isOpen,onRequestClose}: NewTransactionModalsProps){
    
    const [type,setType] = useState('deposit'); 


    
    const [title,setTitle] = useState('');
    const [value,setValue] = useState(0);
    const [category,setCategory] = useState('');
    
    


    function handleCreateNewTransaction(event: FormEvent){
    event.preventDefault();         
    const data = {
        title,
        value,
        category,
        type,
    };

    api.post('/transactions', data)

    } 

    
    return (
        <Modal
        isOpen={isOpen}
        onRequestClose={onRequestClose}
        overlayClassName="react-modal-overlay"
        className="react-modal-content"
        >
        <button type='button' onClick={onRequestClose} className="react-modal-close">
            X
        </button>

        <Container onSubmit={handleCreateNewTransaction}>
        <h2>Cadastrar</h2>
        <input placeholder='Titulo' value={title} onChange={event => setTitle(event.target.value)}></input>
        <input placeholder='Valor' value={value} onChange={event => setValue(Number(event.target.value))}type="number"></input>
        <TransactionTypeContainer>
            <RadioBox 
            type='button' 
            isActive={type === 'deposit'}
            activeColor="green"
            onClick={()=> {setType('deposit');}}>
            <span>Entrada</span>
            </RadioBox>
            
            
            <RadioBox 
            type='button' 
            isActive={type === 'withdraw'}
            activeColor="red"
            onClick={()=> {setType('withdraw');}}>
            <span>Saida</span>
            </RadioBox>
        </TransactionTypeContainer>
        <input placeholder='Categoria' value={category} onChange={event => setCategory(event.target.value)}></input>
        <button type="submit">
            Cadastrar 
        </button>
        </Container>
        </Modal>
    );
};