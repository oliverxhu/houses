var React = require('react');
import { Link } from 'react-router-dom';
class About extends React.Component{
    constructor(){
        super();
    }

    render(){
        return(
            <div>
                <Link to={'/'}>Home</Link>
                <h2>About this site</h2>
            </div>
        );
    }
}

module.exports = About;