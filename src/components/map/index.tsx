'use client'
import { MapContainer, Marker, Popup, TileLayer } from "react-leaflet";

const Map = () => {
    
  return (
          <MapContainer style={{ height: "1000px", width: "100%" }} center={[54, 18]} zoom={13} scrollWheelZoom={true}>
          <TileLayer
            attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          />
          <Marker position={[51.505, -0.09]}>
            <Popup>
              A pretty CSS3 popup. <br /> Easily customizable.
            </Popup>
          </Marker>
        </MapContainer>
  );
};

export default Map;