var React = require('react');

class SearchItem extends React.Component{
    constructor(){
        super();
    }

    render() {
        return (
            <div>
                <form id="location-search" onSubmit={this.handleSubmit}>
                    <input type="text" required ref="newItem"/>
                    <input type="submit" value="Submit" onClick={this.handleSubmit}/>
                </form>
            </div>
        );
    }

    handleSubmit(e){
        e.preventDefault(); // stop normal behaviour of submit button, ie. don't reload page
        // get the props from other views

    };

}

module.exports = SearchItem;