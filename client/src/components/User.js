import React from 'react';
import {ListComponent} from './ListComponent';

export default class UserLists extends React.Component{
    state = { lists: [], loading: true }

    async componentDidMount(){
        const config = {
            headers: {
                'Content-Type': 'application/json'
            }
        }
        config.headers['Authorization'] = 'Bearer ' + localStorage.getItem('token');

        var url = 'http://127.0.0.1:8000/api/v1/list';
        const response = await fetch(url, config);
        const data = await response.json();
        console.log(data);
        this.setState({lists: data, loading: false});
    }

    render() 
    {
        const listsApi = this.state.lists;
        return (
            <div>
                {listsApi.map(list => <ListComponent key={list.id} listName={list.name} items={list.item_set} />)}
            </div>
        )
    }
}