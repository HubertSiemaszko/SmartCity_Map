import {Position} from "@/types/Position";

export const getPosition: Promise<Position> = new Promise(function (resolve, reject) {
    navigator.geolocation.getCurrentPosition((position) => {
        const pos: Position = {
            latitude: position.coords.latitude, //DEFAULT GD
            longitude: position.coords.longitude,
            accuracy: position.coords.accuracy,
        };
        resolve(pos)
    }, function (error) {
        reject(error);
    });
})
