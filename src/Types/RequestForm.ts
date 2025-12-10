
export type RequestForm = {
    name: string
    surname: string
    pesel: number
    description: string
    category: categoryTypes
    latitude: number
    longitude:number
}

export const categoryArray = ["Other","Public Services","Cultural Events","communication in frastructure","BuilidngInfrastructure"];
export type categoryTypes = typeof categoryArray[number];