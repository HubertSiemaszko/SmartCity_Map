'use client';
import {
    MapContainer,
    Marker,
    Popup,
    TileLayer,
    useMap,
    useMapEvent,
} from 'react-leaflet'
import 'leaflet/dist/leaflet.css'
import 'leaflet-defaulticon-compatibility'
import 'leaflet-defaulticon-compatibility/dist/leaflet-defaulticon-compatibility.css'
import { useEffect, useState } from 'react'
import { Icon } from 'leaflet'
import markersData from '../data/markers.json'

const MovingMarker = ({
                          handleLoc,
                          loc,
                      }: {
    handleLoc: (loc: ILoc) => void
    loc: ILoc
}) => {
    useMapEvent('click', (event) => {
        handleLoc({ lat: event.latlng.lat, lon: event.latlng.lng })
    })

    if (loc)
        return (
            <Marker
                position={[loc.lat, loc.lon]}
                icon={
                    new Icon({
                        iconUrl: 'markers/blue_icon.png',
                        iconSize: [20, 35],
                        iconAnchor: [12, 41],
                        popupAnchor: [1, -34],
                        shadowSize: [41, 41],
                    })
                }
            >
                <Popup>
                    <div className="flex flex-col">
                        <span>lat: {loc.lat.toFixed(2)}</span>
                        <span>lon: {loc.lon.toFixed(2)}</span>
                    </div>
                </Popup>
            </Marker>
        )
}

const Recenter = ({ loc }: { loc: ILoc }) => {
    const map = useMap()
    useEffect(() => {
        map.setView([loc.lat, loc.lon])
    }, [loc])

    return null
}

const Markers = () => {
    return (
        <>
            {markersData.map((marker) => (
                <Marker
                    position={[marker.loc.lat, marker.loc.lon]}
                    icon={
                        new Icon({
                            iconUrl: marker.icon,
                            iconSize: [30, 55],
                            iconAnchor: [12, 41],
                            popupAnchor: [1, -34],
                            shadowSize: [41, 41],
                        })
                    }
                >
                    <Popup>
                        <span>{marker.title}</span>
                    </Popup>
                </Marker>
            ))}
        </>
    )
}

const Map = ({ isDark }: { isDark: boolean }) => {
    const [loc, setLoc] = useState<ILoc>({ lat: 48.85, lon: 2.3 })
    const handleLoc = (loc: ILoc) => {
        setLoc(loc)
    }

    return (
        <MapContainer
            center={[48.85, 2.3]}
            zoom={10}
            scrollWheelZoom={true}
            style={{
                height: '100%',
                width: '100%',
                background: isDark ? '#222' : '#fff',
                zIndex: 1,
            }}
        >
            <TileLayer
                url={
                    isDark
                        ? 'https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png?api_key=7b793037-9ccb-4ca8-8088-667624148395'
                        : 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
                }
                attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://stadiamaps.com/" target="_blank">Stadia Maps</a>'
            />
            <MovingMarker handleLoc={handleLoc} loc={loc} />
            <Recenter loc={loc} />
            <Markers />
        </MapContainer>
    )
}

export default Map
