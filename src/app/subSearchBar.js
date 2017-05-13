var React = require('react');

class SubSearchBar extends React.Component{
    constructor(){
        super();
    }

    render(){
        return(
            <div>
                <form>
                    <select id="living-type" placeholder="Rental" ref="living-type">
                        <option>Rental</option>
                        <option>Residential</option>
                    </select>
                    <select id="room" placeholder="Number of rooms" ref="rooms">
                        <option>1</option>
                        <option>2</option>
                        <option>3</option>
                        <option>4+</option>
                    </select>
                    <select id="property-type" placeholder="Property Type" ref="property-type">
                        <option>House</option>
                        <option>Unit</option>
                        <option>Townhouse</option>
                        <option>Flat</option>
                    </select>
                    <select id="min-price" ref="min-price">
                        <option>100k</option>
                        <option>200k</option>
                    </select>
                    <select id="max-price">
                        <option>100k</option>
                        <option>200k</option>
                    </select>
                </form>
            </div>
        );
    }
}

module.exports = SubSearchBar