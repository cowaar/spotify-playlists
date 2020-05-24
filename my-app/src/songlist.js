import React, { Component } from 'react';

import Card from 'react-bootstrap/Card'
import CardDeck from 'react-bootstrap/CardDeck'
import axios from 'axios'


class Songlist extends Component {
    constructor(props) {
        super(props);
        this.state = {
            items: [],
        }
    }


    componentDidMount() {
        axios.get('http://localhost:5000/order/energy').then((res) => {
            this.setState({ items: res.data.items });
        });
    }

    render() {
        return (
            <div>
                <CardDeck>{
                    this.state.items.map((item, i) => {

                        return (
                            <div key={i}>



                                <Card style={{ width: '18rem' }}>
                                    <Card.Img src={item.album.images[1].url} />
                                    <Card.ImgOverlay>
                                        <Card.Body>
                                            <Card.Title>{item.name}</Card.Title>
                                            <Card.Text>  {item.artists.map((artist, j) => {
                                                return (
                                                    <span key={j}>{artist.name}</span>
                                                )
                                            }
                                            )}  </Card.Text>

                                        </Card.Body>
                                    </Card.ImgOverlay>
                                </Card>
                            </div>
                        )
                    }
                    )

                }</CardDeck>
            </div>


        );
    }
}
export default Songlist;
