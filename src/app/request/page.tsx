'use client';
import React, {useState} from 'react';
import {SubmitHandler, useForm} from "react-hook-form";
import {RequestForm} from "@/Types/RequestForm";
import {categoryArray} from "@/Types/RequestForm";

//request form is request type
//ogarnij listye dla category
export default function RequestPage() {
    const {register, handleSubmit} = useForm<RequestForm>({});

    const onSubmit: SubmitHandler<RequestForm>=(data)=>{
        console.log(data);
    }
    console.log(categoryArray);

    const array =categoryArray;
    return (
        <form className={"userForm"} onSubmit={handleSubmit(onSubmit)}>
            <input{...register("name")} type="text" placeholder="Name"/>
            <input{...register("surname")} type="text" placeholder="Surname"/>
            <input{...register("pesel")} type="number" placeholder="PESEL"/>
            <input{...register("description")} type="text" placeholder="Description"/>
            <select id="category" name="category" defaultValue="default">

                {/*{}*/}
                <option value="default" disabled hidden></option>
                {
                    array.map(category => {
                        return (
                            <option key={category} value={category}>{category}</option>
                        )
                    })
                }


                {/*<option value="BuilidngInfrastructure">BuilidngInfrastructure</option>*/}
                {/*<option value="CommunicationInfrastructure">CommunicationInfrastructure</option>*/}
                {/*<option value="CulturalEvents">CulturalEvents</option>*/}
                {/*<option value="PublicServices">PublicServices</option>*/}
                {/*<option value="Other">Other</option>*/}
            </select>
            <input{...register("latitude")} type="number" placeholder="Latitude"/>
            <input{...register("longitude")} type="number" placeholder="longitude"/>


        </form>
    );
}
