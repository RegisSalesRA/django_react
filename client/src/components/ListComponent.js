import React from 'react';
import { ItemComponent } from './ItemComponent';

export function ListComponent(props) {
    const items = props.items;
    return (
        <>
            <h2>{props.listName}</h2>
            <ul>
                {items.map(item => <ItemComponent key={item.id} name={item.name} />)}                
            </ul>
        </>
    )
}