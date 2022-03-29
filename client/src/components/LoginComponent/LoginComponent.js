import React from 'react';
import UserLists from '../User';
import './style.css';
import { Form, Button } from 'react-bootstrap';

export default class LoginComponent extends React.Component {
    constructor(props) {
        super(props);
        this.state = { username: '', password: '' };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleChangePassword = this.handleChangePassword.bind(this);
    }

    handleChange(event) {
        this.setState({ username: event.target.value });
    }

    handleChangePassword(event) {
        this.setState({ password: event.target.value });
    }

    handleSubmit(event) {
        var url = "http://127.0.0.1:8000/api/token/";
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username: this.state.username, password: this.state.password })
        };
        fetch(url, requestOptions)
            .then(response => response.json())
            .then(data => {
                localStorage.setItem('token', data.access);
                this.setState({ token: data.access });
            });
        event.preventDefault();
    }

    logout() {
        localStorage.removeItem('token');
        this.setState({ token: null });
    }

    render() {
        var token = localStorage.getItem('token');

        if (!token)
            return (
                <>
                    <div className='ContainerForm'>
                        <div className='ContainerMain'>
                            <div className='Form'>
                                <span>Welcome Django-React</span>
                                <br/>
                                <br/>
                                <Form onSubmit={this.handleSubmit}>
                                    <Form.Group className="mb-3" controlId="formBasicEmail">
                                        <Form.Label>Email address</Form.Label>
                                        <Form.Control type="text" value={this.state.username} onChange={this.handleChange} placeholder="Username" />
                                    </Form.Group>

                                    <Form.Group className="mb-3" controlId="formBasicPassword">
                                        <Form.Label>Password</Form.Label>
                                        <Form.Control type="password" value={this.state.password} onChange={this.handleChangePassword} placeholder="Password" />
                                    </Form.Group>
                                    <br/>
                                <div className='d-grid gap-2'>
                                <Button size="lg" className='botaoLogin' variant="success" type="submit">
                                        Login
                                    </Button>
                                </div>
                                </Form>
                            </div>
                        </div>
                    </div>
                </>
            );
        else
            return (
                <div>
                    <UserLists />
                    <button onClick={() => this.logout()}> Logout </button>
                </div>
            )
    }
}