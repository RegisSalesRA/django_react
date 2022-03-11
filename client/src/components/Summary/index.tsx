import { Container } from "./styles";

export function Summary(){
    return (
        <Container>
            <div>
                <header>
                    <p>Entradas</p>
                    <p>Imagem</p>
                </header>
                <strong>R$1000,00</strong>
            </div>
            <div>
                <header>
                    <p>Saidas</p>
                    <p>Imagem</p>
                </header>
                <strong>R$1000,00</strong>
            </div>
            <div className="highlight-background">
                <header>
                    <p>Total</p>
                    <p>Imagem</p>
                </header>
                <strong>R$1000,00</strong>
            </div>  
        </Container>
    )
}