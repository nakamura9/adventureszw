import React from 'react';
import MiniCalendar from '../components/mini_calendar';
import {BrowserRouter as Router, Route, Link} from 'react-router-dom';
import styles from './sidebar.css';

const sidebar = (props) =>{
    const titleHeight = document.getElementById('title').offsetHeight;
    const height = document.documentElement.clientHeight - titleHeight -2;
    return(
        <div id="sidebar" className={styles.sidebar} style={{height:height}}>
        {props.eventLink ? <a href={props.eventLink}
        className="btn  btn-block"> <i className="fas fa-plus"></i> Create New Event</a> : null}
            <div className="btn-group">            
                {props.showMonth ? 
                    <Link className="btn text-white" 
                    to={`/calendar/month/${props.calendarState.year}/${props.calendarState.month}`}><i className="fa fas-calendar"></i> Month</Link>:null}
                {props.showWeek ?
                    <Link className="btn " 
                    to={`/calendar/week/${props.calendarState.year}/${props.calendarState.month}/${props.calendarState.day}`}>Week</Link> : null}
                {props.showDay ?
                    <Link className="btn " 
                    to={`/calendar/day/${props.calendarState.year}/${props.calendarState.month}/${props.calendarState.day}`}>Day</Link>:null}
            </div>
            <div className="btn-group">
                <button
                    className="btn text-white"
                    onClick={props.prevHandler}>
                        <i className="fas fa-arrow-left"></i>
                </button>    
                <button
                    className="btn text-white"
                    onClick={props.nextHandler}>
                        <i className="fas fa-arrow-right"></i>
                </button>
            </div>
            <div>
                <MiniCalendar 
                    year={props.calendarState.year}
                    month={props.calendarState.month} />
            </div>
            
        </div>
    );
}

export default sidebar;