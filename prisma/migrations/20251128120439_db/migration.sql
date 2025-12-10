-- CreateTable
CREATE TABLE "User" (
    "pesel" INTEGER NOT NULL,
    "surname" TEXT NOT NULL,

    CONSTRAINT "User_pkey" PRIMARY KEY ("pesel")
);

-- CreateTable
CREATE TABLE "Request" (
    "id" SERIAL NOT NULL,
    "category" TEXT NOT NULL,
    "description" TEXT NOT NULL,
    "userPesel" INTEGER NOT NULL,
    "name" TEXT NOT NULL,
    "dateCreated" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "latitude" DOUBLE PRECISION NOT NULL,
    "longitude" DOUBLE PRECISION NOT NULL,

    CONSTRAINT "Request_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "User_pesel_key" ON "User"("pesel");

-- CreateIndex
CREATE UNIQUE INDEX "Request_id_key" ON "Request"("id");

-- AddForeignKey
ALTER TABLE "Request" ADD CONSTRAINT "Request_userPesel_fkey" FOREIGN KEY ("userPesel") REFERENCES "User"("pesel") ON DELETE RESTRICT ON UPDATE CASCADE;
