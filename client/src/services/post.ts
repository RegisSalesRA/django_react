import axios from 'axios';

export const postapi = axios.create({
    baseURL: 'http://localhost:8000/api/v1',
    
})