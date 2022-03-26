import { Container, Content } from './styles';

interface HeaderProps {
    onOpenNewTransactionModal: () => void;
}

export function Header({onOpenNewTransactionModal}: HeaderProps){    

    return (
        <Container>
            <Content>
                <h1>Logo</h1>
            <button type="button" onClick={onOpenNewTransactionModal}>
                Novo Agendamento
            </button>

        </Content>
        </Container>
    )
}