import React from 'react';

export function ItemComponent(props){
    const status = props.status;
    return(
        <>
        <li>{props.name} status: { status ? <div>completo</div> : <div>incompleto</div> } </li>
        </>
    );
}