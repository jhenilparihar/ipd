"use client";
import { useState } from "react";

const Home = () => {
  const [isModalOpen, setIsModalOpen] = useState(false);

  const openModal = () => {
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false);
  };

  return (
    <section className="w-full flex-center flex-col">
      <h1 className="head_text text-center">
        Discover & Plant
        <br className="max-md:hidden" />
        <span className="orange_gradient text-center"> AI-Recommend Crops</span>
        <br className="max-md:hidden" />
      </h1>
      <p className="desc text-center">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras sodales
        velit arcu, a fringilla ex scelerisque at. Proin vehicula, augue vel
      </p>

      <button
        onClick={openModal}
        className="bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded"
      >
        Open Modal
      </button>

      {isModalOpen && (
        <div className="fixed inset-0 flex items-center justify-center z-100">
          <div className="absolute inset-0 " />
          <div className="bg-white flex flex-col p-8 w-[600px] rounded-lg z-10">
            <h2 className="text-3xl text-center font-bold">Enter Values</h2>
            <br />
            <p>Enter values to get AI Recommended crops for your farm</p>
            <br />
            <div className="flex flex-row justify-around items-center">
              <input
                className="border max-w-[200px] px-2 py-1 rounded-lg my-2"
                type="text"
                placeholder="Langitude"
                disabled
              ></input>
              <input
                className="border max-w-[200px] px-2 py-1 rounded-lg my-2"
                type="text"
                placeholder="Longitude"
                disabled
              ></input>
              <button className="bg-blue-500 w-fit h-fit px-3 rounded-lg py-1 text-white">
                Get Location
              </button>
            </div>
            <button
              onClick={closeModal}
              className="bg-red-500 hover:bg-red-600 text-white font-semibold mt-4 py-2 px-4 rounded"
            >
              Close Modal
            </button>
          </div>
        </div>
      )}
    </section>
  );
};
export default Home;
