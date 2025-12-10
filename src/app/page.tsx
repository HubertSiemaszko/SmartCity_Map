'use client';
import dynamic from "next/dynamic";

const Map = dynamic(() => import('../components/map'), { 
  ssr: false,
  loading: () => <p>Ładowanie mapy...</p>
});

export default function Home() {
  return <Map></Map>
}
